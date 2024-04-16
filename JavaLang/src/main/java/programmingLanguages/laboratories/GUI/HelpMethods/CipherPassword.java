package programmingLanguages.laboratories.GUI.HelpMethods;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

public class CipherPassword {
    public static String encryptPassword(String password) {
        // Создаем объект MessageDigest с использованием алгоритма SHA-256
        MessageDigest md;
        try {
            md = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }

        // Преобразуем пароль в байтовый массив и вычисляем хэш-значение
        byte[] hash = md.digest(password.getBytes());

        // Кодируем хэш-значение в Base64 и выводим на экран
        return Base64.getEncoder().encodeToString(hash);
    }
}
