##########################################################################################
# IMPORTS
# Some generative AI assistance has been used in crafting this scraping code

import requests
import csv
import time
import os


##########################################################################################
# SETTINGS

# Bearer Token is stored as an environment variable.
# Saved tied to individual X developer environment
# All tweets collected 08/20/2026
BEARER_TOKEN = os.environ["X_BEARER_TOKEN"]

OUTPUT_FILE = "florence_tweets.csv"

# Maximum number of tweets to save in this test.
# Starting with 4000 and later narrowing down to 1000; code is edited to ensure there are no repeat tweets
TARGET_TWEETS = 4000

# X uses UTC for API timestamps.
START_TIME = "2018-08-31T00:00:00Z"
END_TIME   = "2018-10-01T00:00:00Z"

SEARCH_URL = "https://api.x.com/2/tweets/search/all"


##########################################################################################
# SEARCH TERMS

# Some overlap kept between different search queries due to nature of data being collected (obtaining differing responses to warning and evacuation messages)

SEARCH_QUERIES = [

    '"Hurricane Florence" -is:retweet',

    '"Hurricane Florence" NWS -is:retweet',

    '"Hurricane Florence" National Weather Service -is:retweet',

    '"Hurricane Florence" FEMA -is:retweet',

    '"Hurricane Florence" Federal Emergency Management Agency -is:retweet',

    '"Hurricane Florence" evacuation -is:retweet',

    '"Hurricane Florence" warning -is:retweet',

    '"Hurricane Florence" flood -is:retweet',

    '"Hurricane Florence" tornado -is:retweet',

    '"Hurricane Florence" "storm surge" -is:retweet',

    '"Hurricane Florence" alert -is:retweet',

    '"Florence" hurricane -is:retweet',

    '"Florence" category -is:retweet',

    '"Florence" evacuation -is:retweet',

    '"Florence" warning -is:retweet',

    '"Florence" "storm surge" -is:retweet',

    '"Florence" flooding -is:retweet',

    '"Florence" tornado -is:retweet',

    '#HurricaneFlorence -is:retweet',

    '#Florence hurricane -is:retweet'

]


##########################################################################################
# TIME WINDOWS

TIME_WINDOWS = [

    ("2018-08-31T00:00:00Z", "2018-09-03T00:00:00Z"),

    ("2018-09-03T00:00:00Z", "2018-09-06T00:00:00Z"),

    ("2018-09-06T00:00:00Z", "2018-09-09T00:00:00Z"),

    ("2018-09-09T00:00:00Z", "2018-09-12T00:00:00Z"),

    ("2018-09-12T00:00:00Z", "2018-09-15T00:00:00Z"),

    ("2018-09-15T00:00:00Z", "2018-09-18T00:00:00Z"),

    ("2018-09-18T00:00:00Z", "2018-09-21T00:00:00Z"),

    ("2018-09-21T00:00:00Z", "2018-09-24T00:00:00Z"),

    ("2018-09-24T00:00:00Z", "2018-09-27T00:00:00Z"),

    ("2018-09-27T00:00:00Z", "2018-10-01T00:00:00Z")

]


##########################################################################################
# API REQUEST

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}


def search_tweets(query, start_time, end_time, remaining):

    tweets = []

    next_token = None


    while len(tweets) < remaining:

        params = {

            "query": query,

            "start_time": start_time,

            "end_time": end_time,

            # X allows up to 100 results per request.
            "max_results": min(100, remaining - len(tweets)),

            "tweet.fields":
                "id,text,created_at,author_id,"
                "conversation_id,in_reply_to_user_id,"
                "lang,public_metrics,referenced_tweets",

            "expansions":
                "author_id"
        }


        if next_token:

            params["next_token"] = next_token


        response = requests.get(
            SEARCH_URL,
            headers=headers,
            params=params
        )


        # --------------------------------------------------------------
        # HANDLE API ERRORS
        # --------------------------------------------------------------

        if response.status_code != 200:

            print(
                "\nAPI ERROR:",
                response.status_code,
                response.text
            )

            break


        # --------------------------------------------------------------
        # PROCESS RESPONSE
        # --------------------------------------------------------------

        data = response.json()

        batch = data.get("data", [])

        tweets.extend(batch)


        print(
            f"Query: {query}\n"
            f"Time period: {start_time} → {end_time}\n"
            f"Retrieved this request: {len(batch)}\n"
            f"Retrieved for this search: {len(tweets)}"
        )


        # --------------------------------------------------------------
        # CHECK FOR MORE RESULTS
        # --------------------------------------------------------------

        next_token = data.get(
            "meta",
            {}
        ).get(
            "next_token"
        )


        if not next_token:

            print(
                "No more tweets available for this "
                "query/time period."
            )

            break


        # Small pause between requests.
        time.sleep(1)


    return tweets

##########################################################################################
# COLLECT TWEETS

# Dictionary allows us to automatically remove duplicate tweets.
all_tweets = {}


for start_time, end_time in TIME_WINDOWS:

    print("\n" + "=" * 80)

    print(
        f"TIME WINDOW: "
        f"{start_time} → {end_time}"
    )

    print("=" * 80)


    for query in SEARCH_QUERIES:

        # --------------------------------------------------------------
        # STOP IF WE ALREADY HAVE ENOUGH UNIQUE TWEETS
        # --------------------------------------------------------------

        if len(all_tweets) >= TARGET_TWEETS:

            break



        # Ensures that we don't collect large amounts of tweets within loop 
        
        remaining = TARGET_TWEETS - len(all_tweets)


        print("\nSEARCHING:")
        print(query)

        print(
            f"Still needed: {remaining}"
        )


        # --------------------------------------------------------------
        # SEARCH
        # --------------------------------------------------------------

        results = search_tweets(
            query,
            start_time,
            end_time,
            remaining
        )


        # --------------------------------------------------------------
        # STORE RESULTS
        # --------------------------------------------------------------

        for tweet in results:

            tweet_id = tweet["id"]


            # Record how this tweet was found.
            tweet["search_window"] = (
                f"{start_time} to {end_time}"
            )

            tweet["search_query"] = query


            # Dictionary automatically removes duplicates.
            all_tweets[tweet_id] = tweet


        print(
            f"Unique tweets collected so far: "
            f"{len(all_tweets)}"
        )


        time.sleep(1)


    # --------------------------------------------------------------
    # STOP AFTER COMPLETING ENOUGH TWEETS
    # --------------------------------------------------------------

    if len(all_tweets) >= TARGET_TWEETS:

        print(
            "\nTarget number of unique tweets reached."
        )

        break


##########################################################################################
# ORGANIZE DATA

# Convert dictionary to list.
tweets = list(all_tweets.values())


# Sort tweets chronologically.
tweets.sort(
    key=lambda x: x.get("created_at", "")
)


# Limit number of tweets saved.
tweets = tweets[:TARGET_TWEETS]


##########################################################################################
# SAVE CSV

fieldnames = [

    "tweet_id",
    "created_at",

    "search_window",
    "search_query",

    "author_id",
    "conversation_id",
    "in_reply_to_user_id",

    "language",
    "text",

    "retweet_count",
    "reply_count",
    "like_count",
    "quote_count"
]


with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8-sig"
) as csvfile:

    writer = csv.DictWriter(
        csvfile,
        fieldnames=fieldnames
    )


    # Write column names.
    writer.writeheader()


    # Write tweets.
    for tweet in tweets:

        metrics = tweet.get(
            "public_metrics",
            {}
        )


        writer.writerow({

            "tweet_id":
                tweet.get("id"),

            "created_at":
                tweet.get("created_at"),

            "search_window":
                tweet.get("search_window"),

            "search_query":
                tweet.get("search_query"),

            "author_id":
                tweet.get("author_id"),

            "conversation_id":
                tweet.get("conversation_id"),

            "in_reply_to_user_id":
                tweet.get("in_reply_to_user_id"),

            "language":
                tweet.get("lang"),

            "text":
                tweet.get("text"),

            "retweet_count":
                metrics.get(
                    "retweet_count",
                    0
                ),

            "reply_count":
                metrics.get(
                    "reply_count",
                    0
                ),

            "like_count":
                metrics.get(
                    "like_count",
                    0
                ),

            "quote_count":
                metrics.get(
                    "quote_count",
                    0
                )
        })


##########################################################################################
# FINISHED

print("\n" + "=" * 80)
print("COLLECTION COMPLETE")
print("=" * 80)

print(
    f"Tweets saved: {len(tweets)}"
)

print(
    f"File: {OUTPUT_FILE}"
)

print(
    f"Unique tweets collected before limit: "
    f"{len(all_tweets)}"
)