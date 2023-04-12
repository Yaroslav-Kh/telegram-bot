
function TgApi(tgApi) 
{

    this.api = tgApi;

    this.unsafe = () => 
    {
        return this.api.initDataUnsaf;
    }

    this.user = () =>
    {
        return this.api.initDataUnsafe.user;
    }


    this.send = (data) => {

        return this.api.sendData(JSON.stringify(data));
    }

    this.close = () => {
        return this.api.close();
    }

}