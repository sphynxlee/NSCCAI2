// a React component  is a function that returns TSX(HTML + JSX)

// import { useState } from "react";
import "./Temperature.css";
import { ThemeProps } from "../interface";


export default function Temperature(props: ThemeProps): JSX.Element {

    return (
        <>
            <h2>Temperature Component</h2>
            <p>The theme is: {props.theme}</p>
        </>
    );

}

// export {Temperature}