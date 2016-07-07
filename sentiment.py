from __future__ import print_function
import semantria
import uuid
import time

serializer = semantria.JsonSerializer()
session = semantria.Session("e1eef79b-f58f-4e79-830c-9203ae09a473", "4a2891a0-2df0-4672-b3e9-5392f2b07256", serializer, use_compression=True)
initialTexts = [
  
    "In Lake Louise - a guided walk for the family with Great Divide Nature Tours rent a canoe on Lake Louise or Moraine Lake  go for a hike to the Lake Agnes Tea House. In between Lake Louise and Banff - visit Marble Canyon or Johnson Canyon or both for family friendly short walks. In Banff  a picnic at Johnson Lake rent a boat at Lake Minnewanka  hike up Tunnel Mountain  walk to the Bow Falls and the Fairmont Banff Springs Hotel  visit the Banff Park Museum. The \"must-do\" in Banff is a visit to the Banff Gondola and some time spent on Banff Avenue - think candy shops and ice cream.",
    "On this day in 1786 - In New York City  commercial ice cream was manufactured for the first time."
]


for text in initialTexts:
   doc = {"id": str(uuid.uuid4()).replace("-", ""), "text": text}
   status = session.queueDocument(doc)
   print (status)
   if status == 202:
    print("\"", doc["id"], "\" document queued successfully.", "\r\n")



length = len(initialTexts)

results = []
sentiment = "Neutral"

while len(results) < length:
   print (len(results))
   print("Retrieving your processed results...", "\r\n")
   time.sleep(2)
   # get processed documents
   status = session.getProcessedDocuments()   
   results.extend(status)


for data in results:
   # print document sentiment score
   print("Document ", data["id"], " Sentiment score: ", data["sentiment_score"], "\r\n")
   if ((data["sentiment_score"]) < 0):
    sentiment = "Negative"
    print (sentiment)

   elif((data["sentiment_score"]) > 0) :
   	sentiment = "Positive"
   	print (sentiment)
   
   else:	
   	print (sentiment)
   	pass


   # print document themes
   if "themes" in data:
      print("Document themes:", "\r\n")
      for theme in data["themes"]:
         print("     ", theme["title"], " (sentiment: ", theme["sentiment_score"], ")", "\r\n")

   # print document entities
   if "entities" in data:
      print("Entities:", "\r\n")
      for entity in data["entities"]:
         print("\t", entity["title"], " : ", entity["entity_type"]," (sentiment: ", entity["sentiment_score"], ")", "\r\n")