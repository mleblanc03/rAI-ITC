import logo from '../../assets/logo_rhombusAI.png'
import Sidebar from '../../components/Sidebar';
import FileList from '../../components/FileList';
import Header from '../../components/Header'

function Home() {
  return (
    <div>  
        <Sidebar>
          <img src={logo} alt='RhombusAI logo' className='logo' />
          <h1 className='title'>Intelligent types converter</h1>
          <Header/>
        </Sidebar>
        <h2>Files</h2>
        <div className='layout-inner'>
          <FileList/>
        </div>
    </div>
  )
}

export default Home;