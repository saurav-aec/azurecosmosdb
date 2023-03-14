// STORED PROC - generateRecord
function generateRecord(name, value) {
    var doc = {
        description: name, 
        reading: value,
        stamp: new Date(),
        group: "records"
    };

    // create document
    __.createDocument(__.getSelfLink(), doc, documentCreated);

}

// Callback for createDocument
function documentCreated(error, newDoc) {

    if(error) throw new Error(error.message);

    // getContext() - Gets HTTP Conext
    getContext().getResponse().setBody(newDoc);

}