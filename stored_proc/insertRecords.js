function generateRecords(id,categoryName,item,itemDescription) {
    
    var data = {
        id: id,
        category: categoryName,
        name: item,
        description: itemDescription,
        isComplete: false
    };

    __.createDocument(__.getSelfLink(), data, documentCreated);
}

function documentCreated(err, data) {

    if(err) throw new Error(err.message);

    getContext().getResponse().setBody(data);
}