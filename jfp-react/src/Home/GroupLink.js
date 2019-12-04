import React from 'react';
import { BrowserRouter as Link} from 'react-router-dom';
import Button from 'react-bootstrap/Button';



class GroupLink extends React.Component{
    handleClick = () => {
        this.props.onHeaderClick();
    }
    render(){
        return(
            <div>
                <Button variant="link" onClick={this.handleClick}>{this.props.name}</Button>
            </div>
        )
    }
}

export default GroupLink