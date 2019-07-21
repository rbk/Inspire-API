# READMD

I'm always needing a simple API to pull quotes. So I created one.
The purpose of this website is to provided inspiration through
the words of thought leaders from around the world.

The API can be used for any website for free, forever. ( or until the AWS bill doesn't get paid because I died)

## Data

I found about 5000 quotes from Github.
This is the structures of the data:

```json
{
    "quote": "Whatever the mind of man can conceive and believe, it can achieve.",
    "author": "Napoleon Hill"
}
```


## API Docs

Using the api is simple.

To get all the quotes:

```
HTTP GET /api/quotes

Response {
    [
        ... // All quotes in object
    ]
}
```

To get a single quote

HTTP GET /api/quotes/{id}

Where id is a number between 0 and 5000.

Response {
    "quote": "Whatever the mind of man can conceive and believe, it can achieve.",
    "author": "Napoleon Hill"
}

```


## Setup Website

https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html

https://stackoverflow.com/questions/45044147/use-domain-registered-on-google-domains-to-point-to-amazon-s3-static-website

https://www.gatsbyjs.org/docs/deploying-to-s3-cloudfront/