import './App.css';
import { Search } from './components/search';


function App() {
  return (
    <main className='p-10 bg-gray-50 h-full'>
      <div className='container'>
        <h1 className='font-bold text-4xl mb-5 text-center'>Hometap Code Challenge</h1>
        <Search />
      </div>
    </main>
  )
}

export default App;
