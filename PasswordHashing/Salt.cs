string Salt = GetRandomString(20);

public string GetRandomString(int length) {
    // create random class instance
    Random random = new Random();

    // all chars and numbers as input
    string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    //generate random string for the supplied length
    string str = new string(Enumerable.Repeat(chars, length).Select(s => s[random.Next(s.Length)]).ToArray());

    return str;
}