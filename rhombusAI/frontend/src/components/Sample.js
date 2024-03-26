import React, { useEffect, useState } from 'react'
import {Loader} from '../utils/style/Atoms'
import '../styles/Schema.css'

function Sample({fileID, converted, rows}) {
    const [sample, setSample] = useState({})
    const [isDataLoading, setDataLoading] = useState(false)
    const [error, setError] = useState(null)

    useEffect(() => {
        const fetchData = async () => {
            setDataLoading(true)
            try {
                const url = new URL(`http://127.0.0.1:8000/api/file/${fileID}/sample/`)
                url.search = new URLSearchParams({rows, converted})
                console.log(url)
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error("HTTP error " + response.status);
                }
                const data = await response.json();
                setSample(data.data);
                console.log(data.data)
            } catch (error) {
                console.error("Fetch error: ", error);
                setError(true)
            }
            finally {
                setDataLoading(false);
            }
        };
    
        fetchData();
    }, [fileID, rows]);

    return (
        <div>
            {isDataLoading ? (
                <Loader />
            ) : (
                renderTable()
            )}
        </div>
    );
    
    function renderTable() {
        const headers = Object.keys(sample);
        const maxRows = getMaxRows();
    
        return (
            <table>
                <thead>
                    <tr>
                        {headers.map((key) => (
                            <th key={key}>{key}</th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {Array.from({ length: maxRows }, (_, index) => (
                        <tr key={index}>
                            {headers.map((header, valueIndex) => (
                                <td key={valueIndex}>{String(sample[header][index])}</td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        );
    }
    
    function getMaxRows() {
        return Math.max(
            ...Object.values(sample).map(
                (value) => Math.max(...Object.keys(value).map(Number))
            )
        ) + 1;
    }
}

export default Sample