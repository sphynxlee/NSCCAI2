// a React component  is a function that returns TSX(HTML + JSX)

// import { useState } from "react";
import "./Weather.css";
import Temperature from "../Temperature/Temperature";
import { ThemeProps } from "../interface";



export default function Weather(props: ThemeProps): JSX.Element {

    return (
        <>
            <div style={{backgroundColor: 'lightblue', padding: '10px', margin: '10px', border: '1px solid black', borderRadius: '5px'}} >
                <h2>Halifax</h2>
                <p>The theme is: {props.theme}</p>
                <Temperature theme={props.theme} />
            </div>
        </>
    );

}

// export {Weather}