// we are going to create a new component called WeatherTile
// using a library called React. To distinguish our custom tags
// from regular HTML, we are required to capitalize their names.
// To make a custom HTML tag(React component), we need to create a
// function whose name is the same as the tag we want to create.

import './WeatherTile.css'

function WeatherTile() {

  return (
    <>
      <h1>WeatherTile</h1>
      <img src="" />
      <h3>Halifax</h3>
    </>
  );
}

export default WeatherTile;