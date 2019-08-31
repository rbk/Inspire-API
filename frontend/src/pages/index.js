import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import Image from "../components/image"
import SEO from "../components/seo"


class IndexPage extends React.Component {

    constructor() {
        super()
        this.state = {
            loading: true,
            quote: {}
        }
    }

    componentDidMount() {
        this.getQuote()
        window.addEventListener('click', (e) => {
            this.refs['main-inner'].classList.remove('fade-in-slow')
            this.getQuote()
        })
    }

    getQuote = () => {
        fetch('https://inspire.richardkeller.net/api/quotes/random')
            .then(res => res.json())
            .then(data => {
                console.log(data)
                this.setState({
                    quote: data,
                    loading: false,
                })
                this.refs['main-inner'].classList.add('fade-in-slow')
            })
    }

    render() {
        const {quote, author, id, link} =  this.state.quote
        return (
          <Layout>
            <nav>
                <a href="/" className="logo">InspireAPI</a>
                <a href="/">API</a>
                <a href="/">About</a>
                <a href="/">Contribute</a>
            </nav>
            <div className="main-hero">
                {this.state.loading &&
                    <div>LOADING</div>
                }
                {!this.state.loading &&
                    <a href={link} className="main-hero--inner" ref="main-inner">
                        <h1 className="main-hero--inner--quote">{quote}</h1>
                        <h2 className="main-hero--inner--author">{author}</h2>
                    </a>
                }
            </div>
          </Layout>
        )
    }
}


export default IndexPage
