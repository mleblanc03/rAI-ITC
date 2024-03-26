import { useParams, useLocation } from "react-router-dom";
import Schema from "../../components/Schema";
import Sample from "../../components/Sample";
import logo from '../../assets/logo_rhombusAI.png';
import Sidebar from '../../components/Sidebar';
import Header from '../../components/Header';

function FileAnalysis() {
    const { fileID } = useParams();
    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);
    const url = queryParams.get('url');
    const name = queryParams.get('name');
    const size = queryParams.get('size');
    const rows = 10;
    
    return (
        <div>
            <Sidebar>
                <img src={logo} alt='RhombusAI logo' className='logo' />
                <h1 className='title'>Intelligent types converter</h1>
                <Header/>
            </Sidebar>
            <h1>Analysis</h1>
            <h2>Name: {name}</h2>
            <h3>Size: {size}B</h3>
            <h2>Schema</h2>
            <div>
                <Schema fileID={fileID} />
            </div>
            <h2>Raw sample</h2>
            <div>
                <Sample fileID={fileID} rows={rows} converted={false}/>
            </div>
            <h2>Converted sample</h2>
            <div>
                <Sample fileID={fileID} rows={rows} converted={true}/>
            </div>
        </div>
    );
}

export default FileAnalysis;