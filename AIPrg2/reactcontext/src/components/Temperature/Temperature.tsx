// a React component  is a function that returns TSX(HTML + JSX)

// import { useState } from "react";
import "./Temperature.css";
import { ThemeProps } from "../interface";
import { useContext } from "react";
import { ThemeContext } from "../../contexts/ThemeContext";


export default function Temperature(props: ThemeProps): JSX.Element {

    const theme = useContext(ThemeContext);
    return (
        <>
            <h2>Temperature Component</h2>
            <p>The theme is: {props.theme}</p>
            <p>The theme is: {theme}</p>
        </>
    );

}

// export {Temperature}
// export default Temperature;