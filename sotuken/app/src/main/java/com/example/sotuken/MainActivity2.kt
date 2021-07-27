package com.example.sotuken

import android.content.Intent
import android.os.Bundle
import android.view.View
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity
import androidx.navigation.findNavController
import androidx.navigation.ui.AppBarConfiguration
import androidx.navigation.ui.navigateUp
import androidx.navigation.ui.setupActionBarWithNavController
import com.example.sotuken.databinding.ActivityMain2Binding
import com.example.sotuken.ui.login.LoginActivity

class MainActivity2 : AppCompatActivity() {

            override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.activity_main)
        }

        fun onClickButtonTapped(view: View?) {
            val intent = Intent(this, LoginActivity::class.java)
            startActivity(intent)
        }
    }




