import { Outlet, Link } from "react-router-dom"

function Users () {
    return (
        <div>
            <Outlet context={[1,2,3]} />
            <h1>Users</h1>
            <Link to="1">User 1</Link>
        </div>
    )
}

export default Users