import './App.css'
import Stocks from './components/Stocks/Stocks'
import Weather from './components/Weather/Weather'

function App() {
  // const [count, setCount] = useState(0)
  const currentTheme: string = 'dark';

  return (
    <>
      <Stocks theme={currentTheme} />
      <Weather theme={currentTheme} />
    </>
  )
}

export default App
