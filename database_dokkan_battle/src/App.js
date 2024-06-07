import { Routes, Route} from 'react-router-dom';
import './App.css';
import Inicio from './screens/inicio/inicio';
import Cabecera from './screens/cabecera/cabecera';
import Personajes from './screens/characters/personajes';
import Categorias from './screens/categories/categorias';
import Categoria from './screens/category/categoria';
import Noticias from './screens/noticias/noticias';
import Noticia from './screens/noticia/noticia';
import Banners from './screens/banners/banners';
import Banner from './screens/banner/banner';
import Events from './screens/events/events';
import EventType from './screens/eventType/evenType';
import Event from './screens/event/event';
import NotFound from './screens/notFound/notFound';
import About from './screens/about/about';
import Character from './screens/character/character';

function App() {
  return (
    <Routes>
      <Route path='/' element={<Cabecera />}>
        <Route index element={<Inicio />} />
        <Route path='/characters' element={<Personajes />} />
        <Route path='/character/:CardId' element={<Character />} />
        <Route path='/categories' element={<Categorias />} />
        <Route path='/category/:CategoryID' element={<Categoria />} />
        <Route path='/news' element={<Noticias />} />
        <Route path='/news/:NewsId' element={<Noticia />} />
        <Route path='/banners' element={<Banners />} />
        <Route path='/banners/:BannerID' element={<Banner />} />
        <Route path='/events/:EventTypeName' element={<Events />} />
        <Route path='/eventType' element={<EventType />} />
        <Route path='/event/:EventId' element={<Event />} />
        <Route path='/about' element={<About />} />
      </Route>
        <Route path='*' element={<NotFound />}></Route>
    </Routes>
  );
}

export default App;
