import { useState } from 'react';
import './TheSwitch.css'

interface TheSwitchProps {
    prompt: string;
    btnColor: string;
}

export default function TheSwitch(props: TheSwitchProps): JSX.Element {

    const [count, setCount] = useState(0);

    function IncrementCount () {
        console.log('clicked');
        setCount(count+1);
    }

    return (
        <>
            <button onClick={IncrementCount} className='my_btn'>{props.prompt}</button>
            <div>
                counter: <b>{count}</b>
            </div>
        </>
    );
}

