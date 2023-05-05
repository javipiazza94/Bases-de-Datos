package curso.openwebinar.twitter

import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.Seconds
import org.apache.spark.streaming.twitter.TwitterUtils
import java.util.Date

object Ejercicio_1 extends App {
  
  System.setProperty("twitter4j.oauth.consumerKey", "ZcXWqs5FvPcefZZzoO4QXEuHe")
  System.setProperty("twitter4j.oauth.consumerSecret", "H4gDoPktQD5swklL9QxUKjuJzut5c6oWXPAczbwjaIZwUKXyFM")
  System.setProperty("twitter4j.oauth.accessToken", "1345214701-305Vm2rdTpg30IafUMYNRZx3cOZ4td1wcgiScnq")
  System.setProperty("twitter4j.oauth.accessTokenSecret", "tyf6U3bJijSypSQT4l2hm2xx3OshBTMJ9ZuwkqmNaFWIv")

  val StreamContext = new StreamingContext("local[*]", "TTEspaña", Seconds(30))
  val tweets = TwitterUtils.createStream(StreamContext, None)
  
  val tweetsWindow = tweets.window(Seconds(60))
  
  case class Tweet (created_at: Date, texto:String)
  val español = tweetsWindow.filter(status=> status.getLang.equals("es"))
  .map(status=>Tweet(status.getCreatedAt(), status.getText()))
  
  val tt = español.filter(_.texto.split(" ")contains("Fernando Alonso"))
  
  tt.saveAsTextFiles("C:/Users/javier.puente.ext/Escritorio", "csv")
  
  StreamContext.start()
  StreamContext.awaitTermination()
}