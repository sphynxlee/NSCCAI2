import Home from  './components/Home'
import Users from  './components/Users'
import User from  './components/User'
import Me from  './components/Me'
import UserName from  './components/UserName'
import { Routes,Route,Link} from 'react-router-dom'

function App() {
  return (
    <>
      <nav><Link to="/">[home]</Link> | <Link to="/users">[users]</Link> | <Link to="/me">[me]</Link></nav>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/users/" element={<Users userlist={[10,21,33]} userName ={"haha123"}/>}>
            <Route path=":id" element={<User/>}/>
            <Route path=":name" element={<UserName/>}/>
        </Route>
        <Route path="/me" element={<Me/>}/>
      </Routes>
    </>
  )
}

export default App
