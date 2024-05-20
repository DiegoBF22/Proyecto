import { Routes, Route} from 'react-router-dom';
import './App.css';
import Inicio from './screens/inicio/inicio';
import Cabecera from './screens/cabecera/cabecera';
import Personajes from './screens/characters/personajes';

function App() {
  return (
    <Routes>
      <Route path='/' element={<Cabecera />}>
        <Route index element={<Inicio />} />
        <Route path='/characters' element={<Personajes />} />
      </Route>
    </Routes>
  );
}

export default App;
