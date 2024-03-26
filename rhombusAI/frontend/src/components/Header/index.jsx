import {Link} from 'react-router-dom';

function Header() {
    return (
        <div>
            <nav>
                <Link to="http://127.0.0.1:8000/data_type_converter/">Home</Link>
                <Link to="/">Dashboard</Link>
                <Link to="http://127.0.0.1:8000/data_type_converter/upload/">Upload file</Link>
            </nav>
        </div>
    )
}
export default Header;