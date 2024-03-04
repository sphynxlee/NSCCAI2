import { Outlet , Link} from "react-router-dom"
import React from 'react'
import PropTypes from 'prop-types';

function Users(props)
{
    return(
        <>
        <div id="left" style={{float:"left",width:"40vw"}}>
            <h1>Users</h1>
            {props.userlist.map((uid)=>{
                return(<React.Fragment key={uid}><Link to={`/users/${uid}`}>User {uid}</Link><br/></React.Fragment>)
            })}

            <Link to={`/username/${props.userName}`}>User {props.userName}</Link>
        </div>

        <div id="right" style={{float:"right",width:"40vw"}}>
            <Outlet context={props.userlist}/>
        </div>

        <div id="right" style={{float:"right",width:"40vw"}}>
            <Outlet context={props.userName}/>
        </div>

        </>
    )
}

Users.propTypes = {
    userlist: PropTypes.array.isRequired,
    userName: PropTypes.string.isRequired,
};

export default Users