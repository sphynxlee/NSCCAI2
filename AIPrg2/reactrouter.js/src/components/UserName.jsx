import { useOutletContext, useParams } from "react-router-dom"

function User()
{
    const context = useOutletContext()
    const {userName} = useParams()
    return (
        <div>
        Users Name:
        {context.map((name, index) => { return (<b key={index}>{name} </b>) })}
        <h3>User {userName} Details</h3>
        </div>
    )
}


export default User