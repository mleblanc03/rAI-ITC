import '../styles/FileItem.css'
import csv_logo from '../assets/csv_logo.png'
import xlsx_logo from '../assets/xlsx_logo.png'
import { useNavigate} from "react-router-dom";

function FileItem({ fileID, url, name, created, size }) {
	const logo = url.endsWith('.csv') ? csv_logo : xlsx_logo
	const sizeMB = size/1000000;
    const navigate = useNavigate();
    const goToFileAnalysis = () => {
        const params = new URLSearchParams({ url, name, size }).toString();
        navigate(`/file-analysis/${fileID}?${params}`);
    }
    const getSizeInformation = () => {
        if (sizeMB < 1) {
            return "Small";
        } else if (sizeMB < 10) {
            return "Medium";
        } else {
            return "Large";
        }
    };

	return (
		<li className='file-item'>
			<img className='file-item-cover' src={logo} alt={`${name} cover`} />
			<h3>{name}</h3>
			<ul>
                <li>Created: {new Date(created).toLocaleString()}</li>
                {sizeMB < 1 ? 
                (<li>Size: {size} Bytes</li>) : 
                (<li>Size: {sizeMB} MB</li>)}
                <li>{getSizeInformation()} file</li>
            </ul>
            <button onClick={goToFileAnalysis}>Analysis</button>
		</li>
	)
}

export default FileItem