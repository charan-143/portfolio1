import { Head, Html, Main, NextScript } from "next/document"
import { ColorModeScript } from "@chakra-ui/react"


export default function Document() {
  return (
    <Html>
  <Head>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" rel="stylesheet"/>
</Head>
  <body>
  <ColorModeScript initialColorMode="light"/>
  <Main/>
  <NextScript/>
</body>
</Html>
  )
}
