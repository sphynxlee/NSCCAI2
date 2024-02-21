// a React component  is a function that returns TSX(HTML + JSX)

// import { useState } from "react";
import "./Weather.css";
import Temperature from "../Temperature/Temperature";

export default function Weather(): JSX.Element {

    return (
        <>
            <h2>Weather Component</h2>
            <Temperature />
        </>
    );

}

// export {Weather}