import React, {Component} from 'react';
import config from "./config.json";
import PhoneNumbers from './components/phonenumbers';

class App extends Component {
    render() {
        return (
            <PhoneNumbers phonenumbers={this.state.phonenumbers} />
        )
    }

    state = {
        phonenumbers: []
    };


    componentDidMount() {
        let apiUrl = config.find(item => item.OutputKey === 'GetPhoneNumberApi').OutputValue;
        fetch(apiUrl)
            .then(res => res.json())
            .then((data) => {
                this.setState({ phonenumbers: data })
            })
            .catch(console.log)
    }
}

export default App;

