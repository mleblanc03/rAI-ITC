import React, { useEffect, useState } from 'react'
import {Loader} from '../utils/style/Atoms' 
import FileItem from './FileItem'
import '../styles/FileList.css'

function FileList() {
	const [fileData, setFileData] = useState([])
	const [isDataLoading, setDataLoading] = useState(false)
	const [error, setError] = useState(null)

	useEffect(() => {
        const fetchData = async () => {
            setDataLoading(true)
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/file`);
                if (!response.ok) {
                    throw new Error("HTTP error " + response.status);
                }
                const data = await response.json();
                console.log(data);
                setFileData(data.results);
            } catch (error) {
                console.error("Fetch error: ", error);
                setError(true)
            }
            finally {
                setDataLoading(false);
            }
        };
    
        fetchData();
    }, []);

	return (
		<div className='repertory'>
			{isDataLoading ? (<Loader />) : 
			<ul className='file-list'>
    			{fileData.map((file) => (
					<FileItem
						key={file.pk}
                        fileID={file.pk}
                        url={file.file}
						name={file.file_name}
                        created={file.uploaded_at}
						size={file.file_size}
						schema={file.schema}
					/>
				))}
			</ul>}
		</div>
	)
}

export default FileList