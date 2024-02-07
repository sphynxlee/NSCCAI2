import { useState } from 'react'
import './App.css'
import TheSwitch from './components/TheSwitch/TheSwitch'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <p>test</p>
      <TheSwitch />
    </>
  )
}

export default App
