// a React component  is a function that returns TSX(HTML + JSX)

// import { useState } from "react";
import "./Stocks.css";
import { ThemeProps } from "../interface";

export default function Stocks(props: ThemeProps): JSX.Element {

    return (
        <>
            <h2>Stocks Component</h2>
            <p>The theme is: {props.theme}</p>
        </>
    );

}

// export {Stocks}