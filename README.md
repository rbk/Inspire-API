# Inspire API (inspireapi.com)

## TODO
- [ ] Ability to email API keys
- [ ] Rate limit by API keys
- [ ] Limit my api to my domain
- [ ] Form to request key
- [ ] Create simple on page docs
- [ ] Put API on domain 
    - https://inspireapi.com/quote/{id}
    - https://inspireapi.com/quote/random

***scope creep***

- [ ] Curation contribution notes
- [ ] History API for website -> https://developer.mozilla.org/en-US/docs/Web/API/History_API
- [ ] Add motion and imagery to website
- [ ] Design Inspire logo
- [ ] Setup daily emailer


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
