import TableFrag from  './components/tableFrag'
import ListFrag from  './components/listFrag'
import ImgFrag from  './components/imgFrag'
import './App.css';

function App() {

  const listItems = ['Apple', 'Banana', 'Cherry'];
  return (
    <div className="centered-content">
      <h1>Components in React</h1>
      <ImgFrag src="https://di-uploads-pod19.dealerinspire.com/walkertoyota/uploads/2019/02/Toyota-mud-1800x670.jpg" alt="dirt offroad 4runner" btnColor="red" prompt="Click to change color" />
      <TableFrag />
      <ListFrag listItems={listItems} />
    </div>
  )
}
export default App;
