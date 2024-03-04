import { useOutletContext, useParams } from "react-router-dom"

function User()
{
    const context = useOutletContext()
    const {id} = useParams()
    return(<div>
        All Users:
        {context.map(uid=>{return(<b key={uid}>{uid} </b>)})}
        <h3>User {id} Details</h3>
        </div>)
}


export default User