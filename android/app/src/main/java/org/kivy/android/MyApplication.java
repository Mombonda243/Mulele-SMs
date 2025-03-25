package org.kivy.android;

import android.app.Application;
import com.castarsdk.android.CastarSdk;

public class MyApplication extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        
        // Initialisation du SDK avec ton Client ID
        CastarSdk.Start(this, "CSK****FHQlUQZ"); // Remplace par ton propre Client ID
    }
}
