import { Routes, Route} from 'react-router-dom';
import './App.css';
import Inicio from './screens/inicio/inicio';
import Cabecera from './screens/cabecera/cabecera';

function App() {
  return (
    <Routes>
      <Route path='/' element={<Cabecera />}>
        <Route index element={<Inicio />} />
      </Route>
    </Routes>
  );
}

export default App;
