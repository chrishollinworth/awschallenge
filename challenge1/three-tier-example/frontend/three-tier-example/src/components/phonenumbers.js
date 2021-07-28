import React from 'react'

const PhoneNumbers = ({phonenumbers}) => {
    return (
        <div>
            <center><h1>Phone Number List</h1></center>
            {phonenumbers.map((phonenumber) => (
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{phonenumber.name}</h5>
                        <h6 class="card-subtitle mb-2 text-muted">{phonenumber.phonenumber}</h6>
                    </div>
                </div>
            ))}
        </div>
    )
};

export default PhoneNumbers