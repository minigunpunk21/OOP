export class User {
    constructor(
        public id: string,
        public login: string,
        public hashedPassword: string,
        public email: string,
        public role: 'guest' | 'user' | 'admin',
        public registrationDate: Date
    ) {}
}
