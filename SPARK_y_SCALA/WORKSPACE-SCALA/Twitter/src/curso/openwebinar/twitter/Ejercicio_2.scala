package curso.openwebinar.twitter

import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.Seconds
import org.apache.spark.streaming.twitter.TwitterUtils
import java.util.Date

//Mostrar los 10 tuits de los usuarios con mas seguidores y los mostramos en un fichero en 90s

object Ejercicio_2 extends App {
  
  //Claves de API Twitter
  System.setProperty("twitter4j.oauth.consumerKey", "ZcXWqs5FvPcefZZzoO4QXEuHe")
  System.setProperty("twitter4j.oauth.consumerSecret", "H4gDoPktQD5swklL9QxUKjuJzut5c6oWXPAczbwjaIZwUKXyFM")
  System.setProperty("twitter4j.oauth.accessToken", "1345214701-305Vm2rdTpg30IafUMYNRZx3cOZ4td1wcgiScnq")
  System.setProperty("twitter4j.oauth.accessTokenSecret", "tyf6U3bJijSypSQT4l2hm2xx3OshBTMJ9ZuwkqmNaFWIv")
  
  //Abrimos Streaming

  val StreamContext = new StreamingContext("local[*]", "T10", Seconds(30))
  val tweets = TwitterUtils.createStream(StreamContext, None)
  val tweetsWindow = tweets.window(Seconds(60))
  
  //Creamos clase tuit
  case class Tweet (created_at: Date, usuario: String, texto:String, seguidores: Int)
  
  //filtramos segun los elementos de la clase
  val español = tweetsWindow.filter(status=> status.getLang.equals("es"))
  .map(t=>Tweet(t.getCreatedAt(), t.getUser.getScreenName(), t.getText(), t.getUser.getFollowersCount()))
  
  //ordenamos por seguidores descendente
  val orderFollowers = español.transform(_.sortBy(_.seguidores, false))
  
  //De eos seguidores pillamos los 10 con mas seguidores
  val orderTen = orderFollowers.transform(rdd=>{
     val list = rdd.sortBy(_.seguidores, false).take(10);
     rdd.filter(list.contains)
   }  
       )
   
  //Guardamos el resultado en un CSV
  orderFollowers.saveAsTextFiles("C:/Users/javier.puente.ext/Escritorio", "csv")
  StreamContext.start()
  StreamContext.awaitTermination()
  
}