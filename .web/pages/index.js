import { Fragment, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { connect, E, getAllLocalStorageItems, getRefValue, isTrue, preventDefault, processEvent, refs, set_val, uploadFiles } from "/utils/state"
import "focus-visible/dist/focus-visible"
import { Box, Button, Center, HStack, Image, Input, InputGroup, InputLeftElement, Text, useColorMode, VStack } from "@chakra-ui/react"
import NextHead from "next/head"


export default function Component() {
  const [input_state, setInput_state] = useState({"input_value": "", "is_hydrated": false, "events": [{"name": "input_state.hydrate"}], "files": []})
  const [result, setResult] = useState({"state": null, "events": [], "final": true, "processing": false})
  const [notConnected, setNotConnected] = useState(false)
  const router = useRouter()
  const socket = useRef(null)
  const { isReady } = router
  const { colorMode, toggleColorMode } = useColorMode()
  const focusRef = useRef();
  
  // Function to add new events to the event queue.
  const Event = (events, _e) => {
      preventDefault(_e);
      setInput_state(state => ({
        ...state,
        events: [...state.events, ...events],
      }))
  }

  // Function to add new files to be uploaded.
  const File = files => setInput_state(state => ({
    ...state,
    files,
  }))

  // Main event loop.
  useEffect(()=> {
    // Skip if the router is not ready.
    if (!isReady) {
      return;
    }

    // Initialize the websocket connection.
    if (!socket.current) {
      connect(socket, input_state, setInput_state, result, setResult, router, ['websocket', 'polling'], setNotConnected)
    }

    // If we are not processing an event, process the next event.
    if (!result.processing) {
      processEvent(input_state, setInput_state, result, setResult, router, socket.current)
    }

    // If there is a new result, update the state.
    if (result.state != null) {
      // Apply the new result to the state and the new events to the queue.
      setInput_state(state => ({
        ...result.state,
        events: [...state.events, ...result.events],
      }))

      // Reset the result.
      setResult(result => ({
        state: null,
        events: [],
        final: true,
        processing: !result.final,
      }))

      // Process the next event.
      processEvent(input_state, setInput_state, result, setResult, router, socket.current)
    }
  })

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => Event([E('input_state.hydrate', {})])
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])

  const ref_command = useRef(null); refs['ref_command'] = ref_command;

  return (
  <Fragment><Fragment>
  <Center sx={{"paddingY": "9em", "fontSize": "2em", "textAlign": "center"}}>
  <VStack>
  <Box>
  <Text sx={{"color": "#ff4d4d"}}>
  {input_state.input_value}
</Text>
</Box>
  <HStack>
  <Box>
  <InputGroup>
  <InputLeftElement>
  <Text sx={{"fontSize": 30, "height": "0.8em", "color": "#e28743"}}>
  {`$ `}
</Text>
</InputLeftElement>
</InputGroup>
  <Input focusBorderColor="#e28743" id="command" isRequired={false} onChange={_e => Event([E("input_state.set_input_value", {input_value:_e.target.value})], _e)} placeholder="Hint: type ? to know more..." ref={ref_command} sx={{"width": 600, "height": 65, "fontSize": 25, "paddingLeft": "1.2em", "borderColor": "#abdbe3"}} type="text" value={input_state.input_value}/>
  <Button colorScheme="whatsapp" onClick={_e => Event([E("input_state.get_book_by_title", {})], _e)} sx={{"width": 70, "height": 65, "left": 5, "bottom": 1, "opacity": 50}}>
  <Image src="/play.svg"/>
</Button>
</Box>
</HStack>
</VStack>
</Center>
  <NextHead>
  <title>
  {`search`}
</title>
  <meta content="A Reflex app." name="description"/>
  <meta content="favicon.ico" property="og:image"/>
</NextHead>
</Fragment>
    </Fragment>
  )
}
