import { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

export default function ImgFrag(props) {

    const [btnColor, setBtnColor] = useState('red');

    function changeBgColor () {
        if (btnColor === 'blue') {
            setBtnColor('red');
        } else {
            setBtnColor('blue');
        }
    }

    useEffect(() => {
        console.log('color after click:', btnColor);
    }, [btnColor]);

    return (
        <>
            <img src={props.src} alt={props.alt} style={{width: '400px', height: '200px'}} />
            <br />
            <button onClick={changeBgColor} style={{backgroundColor: btnColor}} className='my_btn'>{props.prompt}</button>
            <div>
            btnColor: <b>{btnColor}</b>
            </div>
        </>
    );
}

ImgFrag.propTypes = {
    src: PropTypes.array.isRequired,
    alt: PropTypes.string.isRequired,
    prompt: PropTypes.string.isRequired,
};