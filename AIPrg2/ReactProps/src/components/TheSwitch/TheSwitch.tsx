import './TheSwitch.css'

interface TheSwitchProps {
    prompt: string;
    btnColor: string;
}

function TheSwitch(props: TheSwitchProps): JSX.Element {
    return (
        <>
            <button className='my_btn'>{props.prompt}</button>
        </>
    );
}

export default TheSwitch;
