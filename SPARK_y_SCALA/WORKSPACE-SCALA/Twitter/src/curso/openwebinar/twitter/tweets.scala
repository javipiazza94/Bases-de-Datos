package curso.openwebinar.twitter

import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.Seconds
import org.apache.spark.streaming.twitter.TwitterUtils

object tweets extends App {

  System.setProperty("twitter4j.oauth.consumerKey", "ZcXWqs5FvPcefZZzoO4QXEuHe")
  System.setProperty("twitter4j.oauth.consumerSecret", "H4gDoPktQD5swklL9QxUKjuJzut5c6oWXPAczbwjaIZwUKXyFM")
  System.setProperty("twitter4j.oauth.accessToken", "1345214701-305Vm2rdTpg30IafUMYNRZx3cOZ4td1wcgiScnq")
  System.setProperty("twitter4j.oauth.accessTokenSecret", "tyf6U3bJijSypSQT4l2hm2xx3OshBTMJ9ZuwkqmNaFWIv")

  val StreamContext = new StreamingContext("local[*]", "IngestaTweets", Seconds(60))
  val tweets = TwitterUtils.createStream(StreamContext, None)

  //Mostrar solo texto
  val texto = tweets.map(status => status.getText())

  texto.print()
  StreamContext.start()
  StreamContext.awaitTermination()
  
}