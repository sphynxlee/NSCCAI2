import { useState, useEffect } from 'react';
import './TheSwitch.css'

interface TheSwitchProps {
    prompt: string;
    btnColor: string;
}

export default function TheSwitch(props: TheSwitchProps): JSX.Element {

    const [count, setCount] = useState(0);

    function IncrementCount () {
        setCount(count+1);
        // console.log('clicked count: ' + count + ' times');
    }

    useEffect(() => {
        console.log('String after increment:', count);
    }, [count]);


    return (
        <>
            <button onClick={IncrementCount} style={{backgroundColor: props.btnColor}} className='my_btn'>{props.prompt}</button>
            <div>
                counter: <b>{count}</b>
            </div>
        </>
    );
}

