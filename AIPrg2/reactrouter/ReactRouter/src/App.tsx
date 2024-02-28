// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'
import Home from './components/Home'
import User from './components/User'
import Users from './components/Users'
import About from './components/About'
import { Routes, Route, Link } from 'react-router-dom'

function App() {
  // const [count, setCount] = useState(0)

  return (
    <>
      <nav>
        {/* [<a href='/'>Home</a>] |
        [<a href='user'>User</a>] |
        [<a href='about'>About</a>] */}

        [<Link to='/'>Home</Link>] |
        [<Link to='users'>Users</Link>] |
        [<Link to='about'>About</Link>]
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/user/:id" element={<User />} /> {/* :id is a parameter, http://localhost:5173/user/123 */}
        <Route path="/users" element={<Users />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </>
  )
}

export default App
