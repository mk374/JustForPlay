import React from 'react';
import Button from 'react-bootstrap/Button';
import WebFont from 'webfontloader'

WebFont.load({
    google: {
      families: ['Titillium Web:300,400,700', 'sans-serif']
    }
});

class GroupLink extends React.Component{
    constructor(props){
        super(props);
        this.state={
          id: this.props.group.gid,
          name: this.props.group.group_name,
          community: this.props.group.community,
          description: this.props.group.description,
          public_private: this.props.group.public_or_private,
        }
      }
    handleClick = (e) => {
        this.props.onClick(e, this.state.id, this.state.name, this.state.community, this.state.description, this.state.public_private);
    }

    render(){
        return(
            <div>
                <style type="text/css">
                    {`
                    .btn-link {
                        color: black;
                        font-size: 50px;
                        font-weight: 200;

                    }
                    .btn-link:hover{
                        color: #a9a9a9;
                    }
                    `}
                </style>
                <Button size="lg" variant="link" onClick={this.handleClick}>{this.state.name}</Button>
            </div>
        )
    }
}

export default GroupLink