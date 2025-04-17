import { User } from '../models/User';

describe('User', () => {
    it('should create a user with correct properties', () => {
        const user = new User('1', 'nikita', 'hashedPassword', 'nikita@example.com', 'user', new Date());

        expect(user.id).toBe('1');
        expect(user.login).toBe('nikita');
        expect(user.email).toBe('nikita@example.com');
        expect(user.role).toBe('user');
    });
});
