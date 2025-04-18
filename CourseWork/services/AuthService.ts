import { User } from '../models/User';
import { hashString } from '../utils/hash';

export class AuthService {
    private users: User[] = [];

    register(login: string, password: string, email: string): User {
        const hashedPassword = hashString(password);
        const newUser = new User(
            (this.users.length + 1).toString(),
            login,
            hashedPassword,
            email,
            'user',
            new Date()
        );
        this.users.push(newUser);
        return newUser;
    }

    authenticate(login: string, password: string): User | null {
        const user = this.users.find(u => u.login === login);
        return user && user.hashedPassword === hashString(password) ? user : null;
    }
}
