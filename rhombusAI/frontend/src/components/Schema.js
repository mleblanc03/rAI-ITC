import React, { useEffect, useState } from 'react'
import {Loader} from '../utils/style/Atoms'
import '../styles/Schema.css'

function Schema({fileID}) {
    const [schema, setSchema] = useState({})
    const [isDataLoading, setDataLoading] = useState(false)
    const [error, setError] = useState(null)

    const typeMapping = {
        "Int64": "Integer",
        "Float64": "Float",
        "boolean": "Boolean",
        "datetime64[ns]": "Date",
        "string": "Text",
        "category": "Category",
    };
 
    useEffect(() => {
        const fetchData = async () => {
            setDataLoading(true)
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/file/${fileID}/schema/`);
                if (!response.ok) {
                    throw new Error("HTTP error " + response.status);
                }
                const data = await response.json();
                setSchema(data.schema);
            } catch (error) {
                console.error("Fetch error: ", error);
                setError(true)
            }
            finally {
                setDataLoading(false);
            }
        };
    
        fetchData();
    }, [fileID]);

    return (
        <div>
            {isDataLoading ? (
                <Loader />
            ) : (
                <table>
                    <thead>
                        <tr>
                            <th>Columns</th>
                            <th>Type</th>
                        </tr>
                    </thead>
                    <tbody>
                        {Object.entries(schema).map(([key, value]) => (
                            <tr key={key}>
                                <td>{key}</td>
                                <td>{typeMapping[value]}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
        </div>
    );
}

export default Schema